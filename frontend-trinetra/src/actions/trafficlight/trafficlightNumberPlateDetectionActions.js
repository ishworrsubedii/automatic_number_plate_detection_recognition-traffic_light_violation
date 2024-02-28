export const START_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT = 'START_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT';
export const STOP_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT = 'STOP_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT';


const getCsrfToken = async () => {
    const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
    const data = await response.json();
    return data.csrfToken;
  };


  const startTrafficlightNumberPlateDetection = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/number_plate_detection/start/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: START_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT, payload: data });
  };
  
  const stopTrafficlightNumberPlateDetection = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/number_plate_detection/stop/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: STOP_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT, payload: data });
  };
  
  export { startTrafficlightNumberPlateDetection, stopTrafficlightNumberPlateDetection };
  