import { Box, IconButton, useTheme, Divider, Card, Typography, Grid, Icon } from "@mui/material";
import { ColorModeContext, tokens } from "../../theme";
import { Link } from "react-router-dom";
import SecurityIcon from '@mui/icons-material/Security';
import { useEffect, useState } from 'react';

const OtherProjects = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);

    const projects = [
        { name: 'Weapon Detection', route: '/weapon-detection', icon: <SecurityIcon /> },
    ];

    return (
        <Grid 
        container 
        spacing={2}
        justifyContent="center"
        style={{ padding: '20px' }}
        >
            {projects.map((project, index) => (
                <Grid item xs={12} sm={6} md={4} lg={3} key={index}>
                    <Link to={project.route} style={{ textDecoration: 'none' }}>
                        <Card sx={{ 
                            width: "100%", 
                            height: "100%", 
                            padding:'20px' , 
                            boxSizing: 'border-box',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            flexDirection: 'column',
                            backgroundColor: theme.palette.primary.main,
                            color: theme.palette.primary.contrastText, 
                        }}>
                            <Box sx={{ fontSize: 60, marginBottom: '20px' }}> 
                                {project.icon}
                            </Box>
                            <Typography variant="h5" component="div">
                                {project.name}
                            </Typography>
                        </Card>
                    </Link>
                </Grid>
            ))}
        </Grid>
    );
}

export default OtherProjects;
