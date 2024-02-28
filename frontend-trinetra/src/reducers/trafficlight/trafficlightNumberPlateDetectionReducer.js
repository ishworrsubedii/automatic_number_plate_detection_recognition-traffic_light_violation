import {START_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT, STOP_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT} from '../../actions/trafficlight/trafficlightNumberPlateDetectionActions';
const initialState = {
    isDetectingNumberPlate: false,
    numberPlateDetectionData: null,
};
const trafficlightNumberPlateDetectionReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT:
            return { 
                ...state, 
                isDetectingNumberPlate: true, 
                numberPlateDetectionData: action.payload 
            };
        case STOP_NUMBER_PLATE_DETECTION_TRAFFIC_LIGHT:
            return { 
                ...state, 
                isDetectingNumberPlate: false, 
                numberPlateDetectionData: action.payload 
            };
        default:
            return state;
    }
};

export default trafficlightNumberPlateDetectionReducer;