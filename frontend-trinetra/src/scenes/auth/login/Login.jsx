import React from 'react';
import {
    Box,
    Paper,
    Divider,
    Typography,
    TextField,
    Button,
    useTheme,
    Checkbox,
    InputLabel,
    IconButton,
    CardContent,
    FormControl,
    OutlinedInput,
    MuiCard,
    InputAdornment,
    MuiFormControlLabel
} from '@mui/material';
import { createTheme } from '@mui/system';
import { tokens } from "../../../theme"

const LoginPage = () => {
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

    const loginButtonStyle = {
        borderRadius: 12,
    };

    return (
        <Box style={containerStyle}>
            <Paper style={paperStyle} elevation={3}>
                <Typography variant="h5" align="center" gutterBottom>
                    Login
                </Typography>
                <form style={formStyle}>
                    <TextField
                        label="Username"
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
                    <Button
                        variant="contained"
                        color="primary"
                        fullWidth
                        style={loginButtonStyle}
                    >
                        Login
                    </Button>
                </form>

            </Paper>
        </Box>
    );
};

export default LoginPage;