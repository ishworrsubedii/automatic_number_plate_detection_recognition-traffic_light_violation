export const START_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT = "START_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT";
export const STOP_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT = "STOP_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT";

const getCsrfToken = async () => {
    const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
    const data = await response.json();
    return data.csrfToken;
  };



  const startTrafficlightDetectionColor = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/traffic_light_color_detection/start/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: START_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT, payload: data });
  };
  
  const stopTrafficlightDetectionColor = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/traffic_light_color_detection/stop/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: STOP_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT, payload: data });
  };
  
  export { startTrafficlightDetectionColor, stopTrafficlightDetectionColor };
  
