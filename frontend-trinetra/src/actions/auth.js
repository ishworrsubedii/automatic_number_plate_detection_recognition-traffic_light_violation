import axios from "axios";

import {
  LOGIN_FAIL,
  LOGIN_SUCCESS,
  LOAD_USER_SUCCESS,
  LOAD_USER_FAIL,
  AUTHENTICATION_FAIL,
  AUTHENTICATION_SUCCESS,
  LOGOUT,
  PASSWORD_RESET_CONFIRM_FAIL,
  PASSWORD_RESET_CONFIRM_SUCCESS,
  PASSWORD_RESET_FAIL,
  PASSWORD_RESET_SUCCESS,
  SIGNUP_FAIL,
  SIGNUP_SUCCESS,
  ACTIVATION_FAIL,
  ACTIVATION_SUCCESS,
} from "./types";

// Function to check if user is authenticated

export const checkAuthenticated = () => async (dispatch) => {
  if (localStorage.getItem("access")) {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    };
    const body = JSON.stringify({ token: localStorage.getItem("access") });
    try {
      const res = await axios.post(
        `${process.env.REACT_APP_API_URL}/auth/jwt/verify/`,
        body,
        config
      );
      if (res.data.code !== "token_not_valid") {
        dispatch({
          type: AUTHENTICATION_SUCCESS,
        });
      } else {
        dispatch({
          type: AUTHENTICATION_FAIL,
        });
      }
    } catch (err) {
      dispatch({
        type: AUTHENTICATION_FAIL,
      });
    }
  } else {
    dispatch({
      type: AUTHENTICATION_FAIL,
    });
  }
};

// Function to load user

export const load_user = () => async (dispatch) => {
  if (localStorage.getItem("access")) {
    const config = {
      headers: {
        "Content-Type": "application/json",
        Authorization: `JWT ${localStorage.getItem("access")}`,
        Accept: "application/json",
      },
    };
    try {
      const res = await axios.get(
        `${process.env.REACT_APP_API_URL}/auth/users/me/`,
        config
      );

      dispatch({
        type: LOAD_USER_SUCCESS,
        payload: res.data,
      });
    } catch (err) {
      dispatch({
        type: LOAD_USER_FAIL,
      });
    }
  } else {
    dispatch({
      type: LOAD_USER_FAIL,
    });
  }
};

// Function to login

export const login = (email, password) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };
  const body = JSON.stringify({ email, password });
  try {
    const res = await axios.post(
      `${process.env.REACT_APP_API_URL}/auth/jwt/create/`,
      body,
      config
    );

    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data,
    });
    dispatch(load_user());
  } catch (err) {
    dispatch({
      type: LOGIN_FAIL,
    });
  }
};

// Function to signup

export const signup =
  (first_name, last_name, email, password, re_password) => async (dispatch) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const body = JSON.stringify({
      first_name,
      last_name,
      email,
      password,
      re_password,
    });

    try {
      const res = await axios.post(
        `${process.env.REACT_APP_API_URL}/auth/users/`,
        body,
        config
      );

      dispatch({
        type: SIGNUP_SUCCESS,
        payload: res.data,
      });
    } catch (err) {
      dispatch({
        type: SIGNUP_FAIL,
      });
    }
  };

// Function to verify user

export const verify = (uid, token) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const body = JSON.stringify({ uid, token });

  try {
    await axios.post(
      `${process.env.REACT_APP_API_URL}/auth/users/activation/`,
      body,
      config
    );

    dispatch({
      type: ACTIVATION_SUCCESS,
    });
  } catch (err) {
    dispatch({
      type: ACTIVATION_FAIL,
    });
  }
};
// Function to reset password

export const reset_password = email => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
  };

  const body = JSON.stringify({ email });

  try {
    await axios.post(
      `${process.env.REACT_APP_API_URL}/auth/users/reset_password/`,
      body,
      config
    );

    dispatch({
      type: PASSWORD_RESET_SUCCESS,
    });
  } catch (err) {
    dispatch({
      type: PASSWORD_RESET_FAIL,
    });
  }
};
// Function to confirm password reset
export const reset_password_confirm =
  (uid, token, new_password, re_new_password) => async (dispatch) => {
    const config = {
      headers: {
        "Content-Type": "application/json",
      },
    };

    const body = JSON.stringify({ uid, token, new_password, re_new_password });

    try {
      await axios.post(
        `${process.env.REACT_APP_API_URL}/auth/users/reset_password_confirm/`,
        body,
        config
      );

      dispatch({
        type: PASSWORD_RESET_CONFIRM_SUCCESS,
      });
    } catch (err) {
      dispatch({
        type: PASSWORD_RESET_CONFIRM_FAIL,
      });
    }
  };

// Function to logout

export const logout = () => (dispatch) => {
  dispatch({
    type: LOGOUT,
  });
};
