import { START_ALPR_TRAFFIC_LIGHT,STOP_ALPR_TRAFFIC_LIGHT } from "../../actions/trafficlight/trafficlightALPRActions";
const initialState = {
    isCapturing: false,
    captureData: null,
};

const trafficlightALPRReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_ALPR_TRAFFIC_LIGHT:
            return { 
                ...state, 
                isCapturing: true, 
                captureData: action.payload 
            };
        case STOP_ALPR_TRAFFIC_LIGHT:
            return { 
                ...state, 
                isCapturing: false, 
                captureData: action.payload 
            };
        default:
            return state;
    }
};

export default trafficlightALPRReducer;
