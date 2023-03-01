import os
import re
import argparse
import time
import requests
from pyChatGPT import ChatGPT
# import yaml
from yaml import load, dump, Loader
import io
import warnings
import shutil
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ["STABILITY_KEY"] = os.getenv("STABILITY_KEY")

def generate_image(cfg:dict)-> None:
    prompt = cfg['imageArgs']['prompt']
    stability_api = client.StabilityInference(
        key=os.environ['STABILITY_KEY'], # API Key reference.
        verbose=True, # Print debug messages.
        engine="stable-diffusion-v1-5", # Set the engine to use for generation. 
        # Available engines: stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0 
        # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-inpainting-v1-0 stable-inpainting-512-v2-0
    )
    answers = stability_api.generate(
        prompt=prompt
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                # images
                image_root = "images" + "/" + str(artifact.seed)+ ".png"
                img.save(image_root) # Save our generated images with their seed number as the filename.
                return image_root

def generate_frontmatter(cfg: dict)-> None:
    # open output file
    output_file = cfg['outputFile']
    with open(output_file, 'w') as f:
        # write frontmatter
        f.write('---\n')
        # get frontmatter
        frontmatter = cfg['frontMatter']
        for key, value in frontmatter.items():
            # jupytext and kernelspec convert items to yaml
            if key in ['jupytext', 'kernelspec']:
                f.write(f'{key}:\n')
                for k, v in value.items():
                    if k in ['text_representation']:
                        f.write(f'{k}:\n')
                        for k2, v2 in v.items():
                            f.write(f' {k2}: {v2}\n')
                        continue
                    f.write(f'  {k}: {v}\n')
                continue
            f.write(f'{key}: {value}\n')
        f.write('---\n')
        # write body
    pass

def use_programming_language(cfg: dict, section_text: str, language: str = None)-> None:
    # get programming language
    programming_language = language or cfg['programmingLanguage']
    # use regex to find plain ``` and replace with ```programming_language
    type_start_line = None
    type_end_line = None
    # replace with code blocks with programming language
    # split lines by \n
    modified_lines = []
    lines = section_text.split('\n')
    for i, line in enumerate(lines):
        if line == '```':
            if type_start_line is None:
                type_start_line = i
                # append modified line
                modified_lines.append(f'```{programming_language}')
            else:
                # odd number of ``` so we are ending a code block
                type_start_line = None
                # append modified line
                modified_lines.append('```')
        else:
            # adjust line if type_start_line is not None
            # remove ` at the beginning of the line and the end of the line
            if type_start_line is not None:
                # check for ` character at the beginning of the line
                if line.strip() != '':
                    if line[0] == '`':
                        line = line[1:]
                    # check for ` character at the end of the line
                    if line[-1] == '`':
                        line = line[:-1]
            modified_lines.append(line)

    return "\n".join(modified_lines)

def try_chatgpt_response(text: str):
    attempts = 0
    while attempts < 3:
        try:
            resp = api.send_message(text)
            return resp
        except Exception as e:
            attempts += 1
            time.sleep(3)
            if attempts == 3:
                raise e
    raise Exception("Failed to get response from ChatGPT")
def generate_body(cfg: dict)-> None:
    # read CHATGPT_TOKEN from os
    CHATGPT_SESSION_TOKEN = os.getenv("CHATGPT_TOKEN")
    # print(CHATGPT_SESSION_TOKEN)
    session_token = CHATGPT_SESSION_TOKEN  # `__Secure-next-auth.session-token` cookie from https://chat.openai.com/chat
    api = ChatGPT(session_token)  # auth with session token
    output_file = cfg['outputFile']
    sections = cfg['sections']
    # send seed prompt if available
    if 'seedPrompt' in cfg:
        seed_prompt = cfg['seedPrompt']
        resp = api.send_message(seed_prompt)
        time.sleep(3)
    with open(output_file, 'a', encoding="utf-8", errors="replace") as f:
        for section in sections:
            # check if str or dict
            if isinstance(section, str):
                resp = api.send_message(section)
                clean_message = use_programming_language(cfg, resp['message'])
            else:
                # assume dict
                # type and src from dict
                input_type = section['type']
                src = section['src']
                language = section.get('language', None)
                if input_type == 'file':
                    # read src from file
                    with open(src, 'r') as src_file:
                        src_text = src_file.read()
                    # check for lines argument
                    if 'lines' in section:
                        lines = section['lines']
                        # make sure lines is a list
                        if isinstance(lines, list):
                            # get lines from src_text
                            src_lines = src_text.split('\n')
                            src_text = "\n".join(src_lines[lines[0]:lines[1]])
                    resp = api.send_message(src_text)
                    clean_message = resp['message']
                    # write original text
                    programming_language = language or cfg['programmingLanguage'] 
                    f.write(f"```{programming_language} \n {src_text} \n ```\n")
                    f.write('\n')
                if input_type == 'url':
                    # load from url
                    src_text = requests.get(src).text
                    if 'lines' in section:
                        lines = section['lines']
                        # make sure lines is a list
                        if isinstance(lines, list):
                            # get lines from src_text
                            src_lines = src_text.split('\n')
                            src_text = "\n".join(src_lines[lines[0]:lines[1]])
                    # check if file should be saved to file
                    if 'saveFile' in section:
                        save_file = section['saveFile']
                        if save_file:
                            # save file to src
                            with open(src, 'w') as src_file:
                                src_file.write(src_text)
                    resp = api.send_message(src_text)
                    clean_message = resp['message']
                    # write original text
                    programming_language = language or cfg['programmingLanguage']
                    f.write(f"```{programming_language} \n {src_text} \n ```\n")
                    f.write('\n')
                if input_type == 'raw':
                    clean_message = src
            f.write(clean_message)
            f.write('\n')
            time.sleep(6)
        # output references
        try:
            references = cfg['references']
            if references:
                f.write('\n')
                f.write('## References\n')
                for reference in references:
                    if 'title' in reference and 'url' in reference:
                        f.write(f"- [{reference['title']}]({reference['url']})\n")
                    else:
                        f.write(f"- {reference}\n")
        except Exception as e:
            print(e)
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str, default='posts/transcribe_youtube_videos.yml')
    args = parser.parse_args()

    image_root = ""
    # valid files exist
    # argparse for file eventually
    with open(args.file, 'r') as f:
        cfg = load(f, Loader=Loader)
    # if file exists skip
    # if not run these functions
    if os.path.exists(cfg['outputFile']):
        print('file exists')
        exit(0)
    # if genImage is true, then makeImage
    if cfg['imageArgs']:
        image_path = generate_image(cfg)
        pass
    
    astro_image_folder = "/imgs/2023"
    # grab basename from image_path
    image_basename = os.path.basename(image_path)
    imgSrc = f"{astro_image_folder}/{image_basename}"
    #
    cfg["frontMatter"]["imgSrc"] = imgSrc
    generate_frontmatter(cfg)
    generate_body(cfg)

    ## cp file to ../astro-tech-blog/${directory}
    try:
        if cfg["postOutput"]:
            # check for postOutput.folder
            # check for postOutput.imgFolder
            # mv cfg['outputFile'] to ../astro-tech-blog/${postOutput.folder}
            post_output_folder = cfg['postOutput']['folder']
            post_output_img_folder = cfg['postOutput']['imgFolder']
            if post_output_folder:
                # copy file to ../astro-tech-blog/${postOutput.folder}
                shutil.copy(cfg['outputFile'], post_output_folder)
                # copy image to ../astro-tech-blog/${postOutput.imgFolder}
            if post_output_img_folder:
                shutil.copy(image_path, post_output_img_folder)
    except Exception as e:
        print(e)
        pass