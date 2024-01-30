import React from "react";
import {
  Box,
  IconButton,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
  Checkbox,
  FormControlLabel,
  FormControl,
  InputLabel,
  OutlinedInput,
  InputAdornment,
  Grid,
} from "@mui/material";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";

const SignupPage = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const containerStyle = {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
  };

  return (
    <Box sx={containerStyle}>
      <Paper elevation={3} sx={{ padding: "40px", width: "800px" }}>
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
        />{" "}
        <Typography
          variant="h1"
          style={{ fontWeight: "bold" }}
          textAlign={"left"}
          marginTop={"100px"}
          marginLeft={"60px"}
        >
          Sign up to become the part of{" "}
          <span style={{ color: colors.greenAccent[500] }}>third eye!</span>
        </Typography>
        <form>
          <Grid
            container
            spacing={2}
            style={{ marginTop: "20px", marginLeft: "60px" }}
          >
            <Grid item xs={6}>
              <TextField
                label="First Name"
                type="text"
                variant="outlined"
                style={{ borderRadius: 50, width: "100%" }}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Last Name"
                type="text"
                variant="outlined"
                style={{ borderRadius: 50, width: "100%" }}
              />
            </Grid>
          </Grid>
          <TextField
            label="Email"
            type="email"
            variant="outlined"
            style={{
              borderRadius: 50,
              width: "80%",
              marginTop: "20px",
              marginLeft: "60px",
            }}
          />
          <Grid
            container
            spacing={2}
            style={{ marginTop: "20px", marginLeft: "60px" }}
          >
            <Grid item xs={6}>
              <TextField
                label="Password"
                type="password"
                variant="outlined"
                style={{ borderRadius: 50, width: "100%" }}
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Retype Password"
                type="password"
                variant="outlined"
                style={{ borderRadius: 50, width: "100%" }}
              />
            </Grid>
          </Grid>
          <FormControlLabel
            control={<Checkbox style={{ color: colors.greenAccent[500] }} />}
            label="I agree with terms and conditions"
            style={{ marginTop: "20px", marginLeft: "60px" }}
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
              Create Free Account
            </Typography>
          </Button>
        </form>
      </Paper>
    </Box>
  );
};

export default SignupPage;
