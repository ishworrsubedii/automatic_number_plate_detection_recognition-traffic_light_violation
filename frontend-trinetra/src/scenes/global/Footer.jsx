import React from "react";
import { Box, Typography, useTheme } from "@mui/material";
import { tokens } from "../../theme";


const CustomFooter = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return (
        <Box
            display="flex"
            justifyContent="space-between"
            alignItems="center"
            p={3}
        >
            <Box display="flex" alignItems="flex-start" >
                <Typography variant="h9" color={colors.primary[300]}>
                    © 2023 Trinetra
                </Typography>
            </Box>
            <Box display="flex" alignItems="center" gap={10} ml={150}>
                <Typography variant="h9" color={colors.primary[300]}>
                    About
                </Typography>
                <Typography variant="h9" color={colors.primary[300]}>
                    Support
                </Typography>
                <Typography variant="h9" color={colors.primary[300]}>
                    Contact Us
                </Typography>
            </Box>
        </Box>
    );
};

export default CustomFooter;