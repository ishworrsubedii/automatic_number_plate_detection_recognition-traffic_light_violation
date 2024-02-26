export const FETCH_ALPR_DATA_REQUEST = 'FETCH_ALPR_DATA_REQUEST';
export const FETCH_ALPR_DATA_SUCCESS = 'FETCH_ALPR_DATA_SUCCESS';
export const FETCH_ALPR_DATA_FAILURE = 'FETCH_ALPR_DATA_FAILURE';

export const fetchAlprData = () => async (dispatch, getState) => {
    if (localStorage.getItem('access')) {
        dispatch({ type: FETCH_ALPR_DATA_REQUEST });

        try {
            const accessToken = getState().auth.accessToken;
            const response = await fetch('http://127.0.0.1:8000/api/alpr/alpr_recognition_data/', {
                headers: {
                    Authorization: `JWT ${localStorage.getItem("access")}`,
                }
            });
            const data = await response.json();
            dispatch({ type: FETCH_ALPR_DATA_SUCCESS, payload: data });
        } catch (error) {
            dispatch({ type: FETCH_ALPR_DATA_FAILURE, payload: error.message });
        }
    }

        else {
            dispatch({
              type: FETCH_ALPR_DATA_FAILURE,
            });
          }
};