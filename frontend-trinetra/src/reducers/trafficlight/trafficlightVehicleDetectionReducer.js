import {START_VEHICLE_DETECTION_TRAFFICLIGHT, STOP_VEHICLE_DETECTION_TRAFFICLIGHT} from '../../actions/trafficlight/trafficlightVehicleDetectionActions';
const initialState = {
    isDetectingVehicle: false,
    vehicleDetectionData: null,
};
const trafficlightVehicleDetectionReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_VEHICLE_DETECTION_TRAFFICLIGHT:
            return { 
                ...state, 
                isDetectingVehicle: true, 
                vehicleDetectionData: action.payload 
            };
        case STOP_VEHICLE_DETECTION_TRAFFICLIGHT:
            return { 
                ...state, 
                isDetectingVehicle: false, 
                vehicleDetectionData: action.payload 
            };
        default:
            return state;
    }
};

export default trafficlightVehicleDetectionReducer;