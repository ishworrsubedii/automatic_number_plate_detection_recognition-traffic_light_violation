import React from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
} from "@mui/material";
import { tokens } from "../../../theme";

import InputAdornment from "@mui/material/InputAdornment";

import EmailIcon from "@mui/icons-material/Email";

import trinetralogo from "../../../assets/trinetra.svg";

const ForgotPassword = ({ forgotPassword }) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const handleReset = (event) => {
    event.preventDefault();
    forgotPassword();
  };

  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "left",
        height: "100vh",
        width: "1000px",
      }}
    >
      <img
        src={trinetralogo}
        alt="Logo"
        style={{
          position: "absolute",
          top: 20,
          left: 20,
          width: "80px",
          height: "80px",
        }}
      />

      <Paper
        elevation={3}
        sx={{
          padding: "40px",
          width: "800px",
        }}
      >
        <Typography
          variant="h1"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"100px"}
          marginLeft={"60px"}
        >
          Forgot your password?
          <div style={{ color: colors.greenAccent[500] }}>No worries!</div>
          <Typography
            variant="h5"
            margin={"20px"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
          >
            Enter your email to reset your password.
          </Typography>
        </Typography>

        <form onSubmit={handleReset}>
          <TextField
            label="Email"
            type="email"
            variant="outlined"
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <EmailIcon
                    style={{ fontSize: 20, color: colors.primary[100] }}
                  />
                </InputAdornment>
              ),
            }}
            style={{
              borderRadius: 50,
              width: "80%",
              marginTop: "20px",
              marginLeft: "60px",
            }}
          />
          <Button
            type="submit"
            variant="contained"
            style={{
              borderRadius: 50,
              width: "80%",
              marginTop: "20px",
              marginLeft: "60px",
              backgroundColor: colors.greenAccent[500],
              color: "black",
            }}
          >
            Reset Password
          </Button>
        </form>
      </Paper>
    </Box>
  );
};

export default ForgotPassword;
