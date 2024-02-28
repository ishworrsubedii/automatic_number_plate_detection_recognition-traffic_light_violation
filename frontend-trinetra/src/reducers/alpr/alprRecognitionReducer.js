import {
  START_ALPR_THREAD,
  STOP_ALPR_THREAD,
  FETCH_ALPR_STATUS,
} from "../../actions/alpr/alprRecognitionActions";

const initialState = {
  isLoading: false,
  loadData: null,
  statusData: null,
};

const alprLoadReducer = (state = initialState, action) => {
  switch (action.type) {
    case START_ALPR_THREAD:
      return {
        ...state,
        isLoading: true,
        loadData: action.payload,
      };
    case STOP_ALPR_THREAD:
      return {
        ...state,
        isLoading: false,
        loadData: action.payload,
      };
    case FETCH_ALPR_STATUS:
      return {
        ...state,
        statusData: action.payload,
      };
    default:
      return state;
  }
};

export default alprLoadReducer;
