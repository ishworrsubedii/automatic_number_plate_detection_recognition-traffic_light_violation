export const FETCH_ALPR_DATA_REQUEST_TRAFFIC_LIGHT = 'FETCH_ALPR_DATA_REQUEST_TRAFFIC_LIGHT';
export const FETCH_ALPR_DATA_SUCCESS_TRAFFIC_LIGHT = 'FETCH_ALPR_DATA_SUCCESS_TRAFFIC_LIGHT';
export const FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT = 'FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT';

export const fetchAlprDataTrafficLight = () => async (dispatch, getState) => {
    if (localStorage.getItem('access')) {
        dispatch({ type: FETCH_ALPR_DATA_REQUEST_TRAFFIC_LIGHT });

        try {
            const response = await fetch('http://127.0.0.1:8000/api/trafficlight/alpr-recognition-result/', {
                headers: {
                    Authorization: `JWT ${localStorage.getItem("access")}`,
                }
            });
            const data = await response.json();
            dispatch({ type: FETCH_ALPR_DATA_SUCCESS_TRAFFIC_LIGHT, payload: data });
        } catch (error) {
            dispatch({ type: FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT, payload: error.message });
        }
    }

        else {
            dispatch({
              type: FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT,
            });
          }
};