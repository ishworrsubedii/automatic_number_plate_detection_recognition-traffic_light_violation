import { FETCH_ALPR_DATA_REQUEST, FETCH_ALPR_DATA_SUCCESS, FETCH_ALPR_DATA_FAILURE } from '../../actions/alpr/alprActions';

const initialState = {
    alprData: [],
    loading: false,
    error: null
};

const alprReducer = (state = initialState, action) => {
    switch (action.type) {
        case FETCH_ALPR_DATA_REQUEST:
            return {
                ...state,
                loading: true,
                error: null
            };
        case FETCH_ALPR_DATA_SUCCESS:
            return {
                ...state,
                alprData: action.payload,
                loading: false,
                error: null
            };
        case FETCH_ALPR_DATA_FAILURE:
            return {
                ...state,
                loading: false,
                error: action.payload
            };
        default:
            return state;
    }
};

export default alprReducer;