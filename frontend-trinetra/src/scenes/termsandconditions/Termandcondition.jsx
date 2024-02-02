import React from 'react';
import { Typography, Container, Box } from '@mui/material';

const TermsAndConditions = () => {
    return (
        <Container>
            <Box my={4}>
                <Typography variant="h4" component="h1" gutterBottom>
                    Terms and Conditions
                </Typography>
                <Typography variant="body1" gutterBottom>
                    Welcome to Trinetra! By accessing or using our services, you agree to comply with and be bound by the following terms and conditions:
                </Typography>

                <Typography variant="h5" component="h2" gutterBottom>
                    1. User Account
                </Typography>
                <Typography variant="body1" gutterBottom>
                    In order to access our services, you must create a user account. You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.
                </Typography>

                <Typography variant="h5" component="h2" gutterBottom>
                    2. Service Usage
                </Typography>
                <Typography variant="body1" gutterBottom>
                    Our services are intended for lawful purposes only. You agree not to use our services for any illegal or unauthorized activities.
                </Typography>

                <Typography variant="h5" component="h2" gutterBottom>
                    3. Intellectual Property
                </Typography>
                <Typography variant="body1" gutterBottom>
                    All intellectual property rights related to our services, including but not limited to trademarks, logos, and software, are owned by Trinetra. You are prohibited from using, copying, or distributing any of our intellectual property without our prior written consent.
                </Typography>

                <Typography variant="h5" component="h2" gutterBottom>
                    4. Privacy
                </Typography>
                <Typography variant="body1" gutterBottom>
                    We respect your privacy and handle your personal information in accordance with our Privacy Policy. By using our services, you consent to the collection, use, and disclosure of your personal information as described in our Privacy Policy.
                </Typography>

                <Typography variant="h5" component="h2" gutterBottom>
                    5. Limitation of Liability
                </Typography>
                <Typography variant="body1" gutterBottom>
                    Trinetra shall not be liable for any direct, indirect, incidental, consequential, or exemplary damages arising from the use or inability to use our services.
                </Typography>
            </Box>
        </Container>
    );
};

export default TermsAndConditions;