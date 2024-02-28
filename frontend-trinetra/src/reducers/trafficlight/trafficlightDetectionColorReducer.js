import {START_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT,STOP_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT} from "../../actions/trafficlight/trafficlightDetectionColorActions";

const initialState = {
    isDetecting: false,
    detectionData: null,
};
const trafficlightDetectionColorReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT:
            return { 
                ...state, 
                isDetecting: true, 
                detectionData: action.payload 
            };
        case STOP_TRAFFICLIGHT_DETECTION_COLOR_TRAFFICLIGHT:
            return { 
                ...state, 
                isDetecting: false, 
                detectionData: action.payload 
            };
        default:
            return state;
    }
}

export default trafficlightDetectionColorReducer;