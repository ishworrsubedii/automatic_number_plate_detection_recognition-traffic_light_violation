export const TRAFFIC_LIGHT_FETCH_NON_DETECTED_VEHICLE_PATH = "TRAFFIC_LIGHT_FETCH_NON_DETECTED_VEHICLE_PATH";
export const TRAFFIC_LIGHT_FETCH_DETECTED_VEHICLE_PATH = "TRAFFIC_LIGHT_FETCH_DETECTED_VEHICLE_PATH";

const getCsrfToken = async () => {
  const response = await fetch("http://127.0.0.1:8000/get-csrf-token/");
  const data = await response.json();
  return data.csrfToken;
};

export const fetchDetectedImagesPathTrafficLight = () => async (dispatch) => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/red-light-violated-vehicles-list/",
      {
        method: "GET",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: TRAFFIC_LIGHT_FETCH_DETECTED_VEHICLE_PATH, payload: data });
  } catch (error) {
    console.error("Error fetching recognized image paths:", error);
  }
};

export const fetchNonDetectedImagesPathTrafficLight = () => async (dispatch) => {
  try {
    const csrfToken = await getCsrfToken();
    const response = await fetch(
      "http://127.0.0.1:8000/api/trafficlight/vehicle-not-detected-image-list/",
      {
        method: "GET",
        headers: {
          Authorization: `JWT ${localStorage.getItem("access")}`,
          "X-CSRFToken": csrfToken,
        },
      }
    );
    const data = await response.json();
    dispatch({ type: TRAFFIC_LIGHT_FETCH_NON_DETECTED_VEHICLE_PATH, payload: data });
  } catch (error) {
    console.error("Error fetching non-recognized image paths:", error);
  }
};
