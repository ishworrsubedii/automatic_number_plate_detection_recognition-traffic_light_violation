import { combineReducers } from "redux";
import auth from "./auth";
import alprReducer from "./alprReducer"
import alprCaptureReducer from "./alprCaptureReducer"
import alprLoadReducer from "./alprLoadReducer"
import alprRecognitionReducer from "./alprRecognitionReducer"
import imagePathFetchReducer from "./imagePathFetchReducer"

export default combineReducers({
    auth,
    alpr: alprReducer ,
    alprCapture: alprCaptureReducer,
    alprLoad: alprLoadReducer,
    alprRecognition: alprRecognitionReducer,
    imagePathFetch: imagePathFetchReducer,



});