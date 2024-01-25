import React from 'react';
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
} from '@mui/material';
import { createTheme } from '@mui/system';
import { tokens } from "../../../theme";

const SignupPage = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const containerStyle = {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh',
    };

    const paperStyle = {
        padding: theme.spacing(3),
        maxWidth: 400,
        backgroundColor: theme.palette.background.default,
        borderRadius: 24,
        boxShadow: theme.shadows[3],
    };

    const formStyle = {
        display: 'flex',
        flexDirection: 'column',
        gap: theme.spacing(2),
    };

    const inputFieldStyle = {
        backgroundColor: theme.palette.mode === 'dark' ? '#333' : '#f0f0f0',
        borderRadius: 8,
    };

    const signupButtonStyle = {
        borderRadius: 12,
    };

    return (
        <Box style={containerStyle}>
            <Paper style={paperStyle} elevation={3}>
                <Typography variant="h5" align="center" gutterBottom>
                    Sign Up
                </Typography>
                <form style={formStyle}>
                    <TextField
                        label="Full Name"
                        variant="outlined"
                        fullWidth
                        style={inputFieldStyle}
                    />
                    <TextField
                        label="Email"
                        type="email"
                        variant="outlined"
                        fullWidth
                        style={inputFieldStyle}
                    />
                    <TextField
                        label="Password"
                        type="password"
                        variant="outlined"
                        fullWidth
                        style={inputFieldStyle}
                    />
                    <FormControl fullWidth variant="outlined" style={inputFieldStyle}>
                        <InputLabel htmlFor="outlined-adornment-confirm-password">Confirm Password</InputLabel>
                        <OutlinedInput
                            id="outlined-adornment-confirm-password"
                            type="password"
                            endAdornment={
                                <InputAdornment position="end">
                                    <IconButton
                                        edge="end"
                                        // Add logic for password visibility toggle if needed
                                    >
                                        {/* Password visibility toggle icon */}
                                    </IconButton>
                                </InputAdornment>
                            }
                            label="Confirm Password"
                        />
                    </FormControl>
                    <FormControlLabel
                        control={<Checkbox color="primary" />}
                        label="I agree to the terms and conditions"
                    />
                    <Button
                        variant="contained"
                        color="primary"
                        fullWidth
                        style={signupButtonStyle}
                    >
                        Sign Up
                    </Button>
                </form>
            </Paper>
        </Box>
    );
};

export default SignupPage;
