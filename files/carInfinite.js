import "./styles.css";

export default function App() {
  return (
    <div xs="12" md="6" data-testid="carOnRoad">
      <div className="carWrapper">
        <img
          src="https://upload.wikimedia.org/wikipedia/commons/3/38/Red_Car_Closed_Window_Cartoon_Vector.svg"
          alt="car"
          className="car"
          data-testid="bookingStatusCar"
        />
      </div>
      <div className="bookingCar">
        <div
          className="infinite"
          style={{
            width: "500px"
          }}
          data-testid="bookingStatusRoad"
        >
          <div className="shadow" />
        </div>
      </div>
    </div>
  );
}
