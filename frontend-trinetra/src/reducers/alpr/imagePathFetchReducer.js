import { FETCH_RECOGNIZED_PATH, FETCH_NON_RECOGNIZED_PATH } from "../../actions/alpr/imagePathFetchActions";

const initialState = {
    recognizedPaths: [],
    nonRecognizedPaths: [],
  };
  
  const imagePathFetchReducer = (state = initialState, action) => {
    switch (action.type) {
      case FETCH_RECOGNIZED_PATH:
        return {
          ...state,
          recognizedPaths: action.payload,
        };
      case FETCH_NON_RECOGNIZED_PATH:
        return {
          ...state,
          nonRecognizedPaths: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default imagePathFetchReducer;
  