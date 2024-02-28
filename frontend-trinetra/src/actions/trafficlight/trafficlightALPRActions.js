export const START_ALPR_TRAFFIC_LIGHT = "START_ALPR_TRAFFIC_LIGHT";
export const STOP_ALPR_TRAFFIC_LIGHT = "STOP_ALPR_TRAFFIC_LIGHT";

const getCsrfToken = async () => {
  const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
  const data = await response.json();
  return data.csrfToken;
};

const startALPRTrafficLight = () => async (dispatch) => {
  const csrfToken = await getCsrfToken();
  const response = await fetch(
    "http://127.0.0.1:8000/api/trafficlight/alpr/start/",
    {
      method: "POST",
      headers: {
        Authorization: `JWT ${localStorage.getItem("access")}`,
        "X-CSRFToken": csrfToken,
      },
    }
  );
  const data = await response.json();
  dispatch({ type: START_ALPR_TRAFFIC_LIGHT, payload: data });
};

const stopALPRTrafficLight = () => async (dispatch) => {
  const csrfToken = await getCsrfToken();
  const response = await fetch(
    "http://127.0.0.1:8000/api/trafficlight/alpr/stop/",
    {
      method: "POST",
      headers: {
        Authorization: `JWT ${localStorage.getItem("access")}`,
        "X-CSRFToken": csrfToken,
      },
    }
  );
  const data = await response.json();
  dispatch({ type: STOP_ALPR_TRAFFIC_LIGHT, payload: data });
};

export { startALPRTrafficLight, stopALPRTrafficLight };