export const START_IMAGE_LOAD = "START_IMAGE_LOAD";
export const STOP_IMAGE_LOAD = "STOP_IMAGE_LOAD";

const getCsrfToken = async () => {
  const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
  const data = await response.json();
  return data.csrfToken;
};

const startImageLoad = () => async (dispatch) => {
  const csrfToken = await getCsrfToken();
  const response = await fetch(
    "http://127.0.0.1:8000/api/alpr/image_load/start/",
    {
      method: "POST",
      headers: {
        Authorization: `JWT ${localStorage.getItem("access")}`,
        "X-CSRFToken": csrfToken,
      },
    }
  );
  const data = await response.json();
  dispatch({ type: START_IMAGE_LOAD, payload: data });
};

const stopImageLoad = () => async (dispatch) => {
  const csrfToken = await getCsrfToken();
  const response = await fetch(
    "http://127.0.0.1:8000/api/alpr/image_load/stop/",
    {
      method: "POST",
      headers: {
        Authorization: `JWT ${localStorage.getItem("access")}`,
        "X-CSRFToken": csrfToken,
      },
    }
  );
  const data = await response.json();
  dispatch({ type: STOP_IMAGE_LOAD, payload: data });
};

export { startImageLoad, stopImageLoad };
