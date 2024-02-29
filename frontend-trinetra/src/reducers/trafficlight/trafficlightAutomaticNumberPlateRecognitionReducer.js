import {FETCH_ALPR_DATA_REQUEST_TRAFFIC_LIGHT,FETCH_ALPR_DATA_SUCCESS_TRAFFIC_LIGHT,FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT} from '../../actions/trafficlight/trafficlightAutomaticNumberPlateRecognitionActions';

const initialState = {
    alprViolationData: [],
    loading: false,
    error: null
};

const alprTrafficLightReducer = (state = initialState, action) => {
    switch (action.type) {
        case FETCH_ALPR_DATA_REQUEST_TRAFFIC_LIGHT:
            return {
                ...state,
                loading: true,
                error: null
            };
        case FETCH_ALPR_DATA_SUCCESS_TRAFFIC_LIGHT:
            return {
                ...state,
                alprViolationData: action.payload,
                loading: false,
                error: null
            };
        case FETCH_ALPR_DATA_FAILURE_TRAFFIC_LIGHT:
            return {
                ...state,
                loading: false,
                error: action.payload
            };
        default:
            return state;
    }
};

export default alprTrafficLightReducer;