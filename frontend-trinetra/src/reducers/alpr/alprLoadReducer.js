import { START_IMAGE_LOAD, STOP_IMAGE_LOAD } from '../actions/alprLoadActions';

const initialState = {
    isLoading: false,
    loadData: null,
};

const alprLoadReducer = (state = initialState, action) => {
    switch (action.type) {
        case START_IMAGE_LOAD:
            return { 
                ...state, 
                isLoading: true, 
                loadData: action.payload 
            };
        case STOP_IMAGE_LOAD:
            return { 
                ...state, 
                isLoading: false, 
                loadData: action.payload 
            };
        default:
            return state;
    }
};

export default alprLoadReducer;
