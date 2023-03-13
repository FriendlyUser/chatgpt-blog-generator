for file in c[0-9]*.md; do
    echo "Converting $file"
    pandoc -f markdown -t html "$file" -o "${file%.md}.html"
done
echo "<html><head>" > combined.html
cat styles.csstml >> combined.html
echo "</head><body>" >> combined.html
cat c[0-9]*.html >> combined.html
echo "</body></html>" >> combined.html
