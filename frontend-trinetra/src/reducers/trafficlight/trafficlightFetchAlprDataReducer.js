import { TRAFFIC_LIGHT_FETCH_RECOGNIZED_PATH, TRAFFIC_LIGHT_FETCH_NON_RECOGNIZED_PATH } from "../../actions/trafficlight/trafficlightFetchAlprDataActions";

const initialState = {
    recognizedPaths: [],
    nonRecognizedPaths: [],
  };
  
  const imagePathFetchTrafficLightReducer = (state = initialState, action) => {
    switch (action.type) {
      case TRAFFIC_LIGHT_FETCH_RECOGNIZED_PATH:
        return {
          ...state,
          recognizedPaths: action.payload,
        };
      case TRAFFIC_LIGHT_FETCH_NON_RECOGNIZED_PATH:
        return {
          ...state,
          nonRecognizedPaths: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default imagePathFetchTrafficLightReducer;
  