export const START_VEHICLE_DETECTION_TRAFFICLIGHT = 'START_VEHICLE_DETECTION_TRAFFICLIGHT';
export const STOP_VEHICLE_DETECTION_TRAFFICLIGHT = 'STOP_VEHICLE_DETECTION_TRAFFICLIGHT';

const getCsrfToken = async () => {
    const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
    const data = await response.json();
    return data.csrfToken;
  };

  const startVehicleDetectionTrafficlight = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/vehicle_detection/start/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: START_VEHICLE_DETECTION_TRAFFICLIGHT, payload: data });
  };
  
  const stopVehicleDetectionTrafficlight = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/vehicle_detection/stop/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: STOP_VEHICLE_DETECTION_TRAFFICLIGHT, payload: data });
  };
  
  export { startVehicleDetectionTrafficlight, stopVehicleDetectionTrafficlight };
  