import React from "react";
import {
  Box,
  Paper,
  Typography,
  TextField,
  Button,
  useTheme,
  Checkbox,
  FormControlLabel,
  Grid,
} from "@mui/material";
import { tokens } from "../../../theme";
import trinetralogo from "../../../assets/trinetra.svg";

const SignupPage = () => {
  const theme = useTheme();
  const colors = tokens(theme.palette.mode);

  const containerStyle = {
    display: "flex",
    justifyContent: "left",
    height: "100vh",
    width: "1000px",
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
        />
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

        <Typography
            variant="h5"
            margin="30px"
            marginLeft={"10%"}
            fontStyle={"inherit"}
            color={colors.primary[100]}
          >
           Join Trinetra and experience the magic firsthand.
          </Typography>
        <form style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          width: "90%",
        
        }}>
          <Grid container spacing={2} sx={{ marginTop: "20px", marginLeft: "60px" }}>
            <Grid item xs={6}>
              <TextField
                label="First Name"
                type="text"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Last Name"
                type="text"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={12}>
              <TextField
                label="Email"
                type="email"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Password"
                type="password"
                variant="outlined"
                fullWidth
              />
            </Grid>
            <Grid item xs={6}>
              <TextField
                label="Retype Password"
                type="password"
                variant="outlined"
                fullWidth
              />
            </Grid>
          </Grid>
          <FormControlLabel
            control={<Checkbox style={{ color: colors.greenAccent[500] }} />}
            label="I agree with terms and conditions"
            sx={{ marginTop: "20px", marginLeft: "60px" }}
          />
          <Button
            type="submit"
            variant="contained"
            color="primary"
            sx={{
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