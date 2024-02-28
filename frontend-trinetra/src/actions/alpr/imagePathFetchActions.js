export const FETCH_RECOGNIZED_PATH = "FETCH_RECOGNIZED_PATH";
export const FETCH_NON_RECOGNIZED_PATH = "FETCH_NON_RECOGNIZED_PATH";

const getCsrfToken = async () => {
  const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
  const data = await response.json();
  return data.csrfToken;
};

export const fetchRecognizedImagesPath = () => async (dispatch) => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/alpr/alpr_recognized_image_paths/",
      {
        method: "GET",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: FETCH_RECOGNIZED_PATH, payload: data });
  } catch (error) {
    console.error("Error fetching recognized image paths:", error);
  }
};

export const fetchNonRecognizedImagesPath = () => async (dispatch) => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/alpr/alpr_non_recognized_image_paths/",
      {
        method: "GET",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: FETCH_NON_RECOGNIZED_PATH, payload: data });
  } catch (error) {
    console.error("Error fetching non-recognized image paths:", error);
  }
};

export default {fetchNonRecognizedImagesPath, fetchRecognizedImagesPath};