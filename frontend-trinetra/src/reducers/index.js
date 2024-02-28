import { combineReducers } from "redux";
import auth from "./auth/auth";
import alprReducer from "./alpr/alprReducer"
import alprCaptureReducer from "./alpr/alprCaptureReducer"
import alprLoadReducer from "./alpr/alprLoadReducer"
import alprRecognitionReducer from "./alpr/alprRecognitionReducer"
import imagePathFetchReducer from "./alpr/imagePathFetchReducer"

import trafficlightCaptureReducer from "./trafficlight/trafficlightCaptureReducer"
import trafficlightDetectionColorReducer from "./trafficlight/trafficlightDetectionColorReducer";
import trafficlightVehicleDetectionReducer from "./trafficlight/trafficlightVehicleDetectionReducer"
import trafficlightNumberPlateDetectionReducer from "./trafficlight/trafficlightNumberPlateDetectionReducer"
import trafficlightALPRReducer from "./trafficlight/trafficlightALPRReducer"


export default combineReducers({
    //auth
    auth,
    //alpt
    alpr: alprReducer ,
    alprCapture: alprCaptureReducer,
    alprLoad: alprLoadReducer,
    alprRecognition: alprRecognitionReducer,
    imagePathFetch: imagePathFetchReducer,
    // traffic light
    trafficLightCapture: trafficlightCaptureReducer,
    trafficLightDetectionColor:  trafficlightDetectionColorReducer,
    trafficLightVehicleDetection: trafficlightVehicleDetectionReducer,
    trafficLightNumberPlateDetection: trafficlightNumberPlateDetectionReducer,
    trafficLightALPR: trafficlightALPRReducer




});