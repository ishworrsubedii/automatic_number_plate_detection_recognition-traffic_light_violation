import {TRAFFIC_LIGHT_FETCH_NON_DETECTED_VEHICLE_PATH,TRAFFIC_LIGHT_FETCH_DETECTED_VEHICLE_PATH} from "../../actions/trafficlight/trafficllightVehicleDetectedNonDetectedActions"

const initialState = {
    recognizedPaths: [],
    nonRecognizedPaths: [],
  };
  
  const imagePathFetchDetectedNonDetectedTrafficLightReducer = (state = initialState, action) => {
    switch (action.type) {
      case TRAFFIC_LIGHT_FETCH_NON_DETECTED_VEHICLE_PATH:
        return {
          ...state,
          imgdetectededPaths: action.payload,
        };
      case TRAFFIC_LIGHT_FETCH_DETECTED_VEHICLE_PATH:
        return {
          ...state,
          imgnondetectededPaths: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default imagePathFetchDetectedNonDetectedTrafficLightReducer;
  