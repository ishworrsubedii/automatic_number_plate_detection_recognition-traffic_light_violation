export const START_CAMERA_CAPTURE = 'START_CAMERA_CAPTURE';
export const STOP_CAMERA_CAPTURE = 'STOP_CAMERA_CAPTURE';

const startCameraCapture = () => async (dispatch) => {
    const response = await fetch('http://127.0.0.1:8000/api/alpr/image_capture/start/', {
        method: 'POST',
        headers: {
            Authorization: `JWT ${localStorage.getItem("access")}`,
        }
    });
    const data = await response.json();
    dispatch({ type: START_CAMERA_CAPTURE, payload: data });
};

const stopCameraCapture = () => async (dispatch) => {
    const response = await fetch('http://127.0.0.1:8000/api/alpr/image_capture/stop/', {
        method: 'POST',
        headers: {
            Authorization: `JWT ${localStorage.getItem("access")}`,
        }
    });
    const data = await response.json();
    dispatch({ type: STOP_CAMERA_CAPTURE, payload: data });
};

export { startCameraCapture, stopCameraCapture };
