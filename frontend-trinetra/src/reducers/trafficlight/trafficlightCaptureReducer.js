import {
  START_CAPTURE_TRAFFICLIGHT,
  STOP_CAPTURE_TRAFFICLIGHT,
} from "../../actions/trafficlight/trafficlightCaptureActions";
const initialState = {
  isCapturing: false,
  captureData: null,
};

const trafficlightCaptureReducer = (state = initialState, action) => {
  switch (action.type) {
    case START_CAPTURE_TRAFFICLIGHT:
      return {
        ...state,
        isCapturing: true,
        captureData: action.payload,
      };
    case STOP_CAPTURE_TRAFFICLIGHT:
      return {
        ...state,
        isCapturing: false,
        captureData: action.payload,
      };
    default:
      return state;
  }
};
export default trafficlightCaptureReducer;
