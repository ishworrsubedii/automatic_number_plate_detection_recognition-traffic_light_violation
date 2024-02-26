import { START_CAMERA_CAPTURE, STOP_CAMERA_CAPTURE } from '../actions/alprCaptureActions';

const initialState = {
    isCapturing: false,
    captureData: null,
};

const alprCaptureReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_CAMERA_CAPTURE:
            return { 
                ...state, 
                isCapturing: true, 
                captureData: action.payload 
            };
        case STOP_CAMERA_CAPTURE:
            return { 
                ...state, 
                isCapturing: false, 
                captureData: action.payload 
            };
        default:
            return state;
    }
};

export default alprCaptureReducer;
