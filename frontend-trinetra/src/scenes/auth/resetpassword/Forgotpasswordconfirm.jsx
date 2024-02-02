import React, { useState } from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import { connect } from "react-redux";
import { reset_password_confirm } from "../../../actions/auth";
import { tokens } from "../../../theme";

import InputAdornment from "@mui/material/InputAdornment";
import VpnKeyIcon from "@mui/icons-material/VpnKey";
import trinetralogo from "../../../assets/trinetra.svg";

const ResetPasswordConfirm = (match,reset_password_confirm) => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);
  const[requestSent, setRequestSent] = useState(false);
  const [formData, setFormData] = useState({
    new_password: "",
    re_new_password: "",
  });

  const { new_password, re_new_password } = formData;

  const onChange = (e) =>
    setFormData({ ...formData, [e.target.name]: e.target.value });

  const onSubmit = (e) => {
    e.preventDefault();

    const uid = match.params.uid;
    const token = match.params.token;

    reset_password_confirm(uid, token, new_password, re_new_password);
    setRequestSent(true);
  };

  if (requestSent) {
    navigator("/");
  }

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
          // margin={'100px'}
        >
          Let us be protected by the
          <div style={{ color: colors.greenAccent[500] }}>third eye!</div>
          <Typography
            variant="h5"
            margin={"20px"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
          >
            Password Reset Confirmation
          </Typography>
        </Typography>

        <form>
            <TextField
              label="New Password"
              type="password"
              variant="outlined"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <VpnKeyIcon
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
              value={new_password}
              onChange={(e) => onChange(e)}
              name="new_password"
              minLength="8"
              required
            />

            <TextField
              label="ReType New Password"
              type="password"
              variant="outlined"
              
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <VpnKeyIcon
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
              value={re_new_password}
              onChange={(e) => onChange(e)}
              name="re_new_password"
              minLength="8"
              required

            />

          <Button
            type="submit"
            variant="contained"
            color="primary"
            style={{
              backgroundColor: colors.greenAccent[500],
              color: colors.primary[500],
              marginTop: "5%",
              marginLeft: "20%",
              height: "5%",
              width: "50%",
              fontSize: "18px",
            }}
          >
            <Typography style={{ fontWeight: "bold" }}>
              Change Password
            </Typography>
          </Button>

          <Box
            display="flex"
            alignItems="center"
            width="80%"
            margin="30px auto"
          >
            <Box
              flexGrow={1}
              borderBottom={1}
              borderColor={colors.primary[200]}
            />
          </Box>
        </form>
      </Paper>
    </Box>
  );
};

export default connect(null,{reset_password_confirm}) (ResetPasswordConfirm);
