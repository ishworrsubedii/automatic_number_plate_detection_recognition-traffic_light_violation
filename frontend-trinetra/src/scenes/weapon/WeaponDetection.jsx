import { Box, IconButton, useTheme, Divider } from "@mui/material";
import { ColorModeContext, tokens } from "../../theme";

const WeaponDetectionService = () => {
    const theme = useTheme();
    const colors = tokens(theme.palette.mode);
    return (
        <div>
            <h1>Weapon Detection Service</h1>
            

        </div>
    );
}
export default WeaponDetectionService;