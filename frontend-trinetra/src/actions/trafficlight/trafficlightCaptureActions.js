export const START_CAPTURE_TRAFFICLIGHT = "START_CAPTURE_TRAFFICLIGHT";
export const STOP_CAPTURE_TRAFFICLIGHT = "STOP_CAPTURE_TRAFFICLIGHT";

const getCsrfToken = async () => {
    const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
    const data = await response.json();
    return data.csrfToken;
  };



  const startCaptureTrafficlight = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/image_capture/start/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: START_CAPTURE_TRAFFICLIGHT, payload: data });
  };
  
  const stopCaptureTrafficlight = () => async (dispatch) => {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/image_capture/stop/",
      {
        method: "POST",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: STOP_CAPTURE_TRAFFICLIGHT, payload: data });
  };
  
  export { startCaptureTrafficlight, stopCaptureTrafficlight };
  
