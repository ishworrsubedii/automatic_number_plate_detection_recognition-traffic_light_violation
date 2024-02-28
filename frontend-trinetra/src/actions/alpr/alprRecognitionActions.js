export const START_ALPR_THREAD = "START_ALPR_THREAD";
export const STOP_ALPR_THREAD = "STOP_ALPR_THREAD";
export const FETCH_ALPR_STATUS = "FETCH_ALPR_STATUS";

const startRecognition = () => async (dispatch) => {
  const response = await fetch("http://127.0.0.1:8000/api/alpr/alpr/start/", {
    method: "POST",
    headers: {
      Authorization: `JWT ${localStorage.getItem("access")}`,
    },
  });
  const data = await response.json();
  dispatch({ type: START_ALPR_THREAD, payload: data });
};

const stopRecognition = () => async (dispatch) => {
  const response = await fetch("http://127.0.0.1:8000/api/alpr/alpr/stop/", {
    method: "POST",
    headers: {
      Authorization: `JWT ${localStorage.getItem("access")}`,
    },
  });
  const data = await response.json();
  dispatch({ type: STOP_ALPR_THREAD, payload: data });
};

const fetchRecognitionStatus = () => async (dispatch) => {
  const response = await fetch("http://127.0.0.1:8000/api/alpr/alpr_status/", {
    method: "GET",
    headers: {
      Authorization: `JWT ${localStorage.getItem("access")}`,
    },
  });
  const data = await response.json();
  dispatch({ type: FETCH_ALPR_STATUS, payload: data });
};

export { startRecognition, stopRecognition, fetchRecognitionStatus };
