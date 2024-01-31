import {
  LOGIN_FAIL,
  LOGIN_SUCCESS,
  LOAD_USER_SUCCESS,
  LOAD_USER_FAIL,
} from "../actions/types";

//auth reducer

const initialState = {
    access: localStorage.getItem("access"),
    refresh: localStorage.getItem("refresh"),
    isAuthenticated: null,
    user: null,
    };

export default function (state = initialState, action) {
    const { type, payload } = action;
    
    switch (type) {
        case LOGIN_SUCCESS:
        localStorage.setItem("access", payload.access); //access the login hash
        localStorage.setItem("refresh", payload.refresh); //access the refresh hash
        return {
            ...state,
            isAuthenticated: true,
            access: payload.access,
            refresh: payload.refresh,
        };
        case LOAD_USER_SUCCESS:
        return {
            ...state,
            isAuthenticated: true,
            user: payload,
        };
        case LOGIN_FAIL:
        case LOAD_USER_FAIL:
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        return {
            ...state,
            access: null,
            refresh: null,
            isAuthenticated: false,
            user: null,
        };
        default:
        return state;
    }
    }