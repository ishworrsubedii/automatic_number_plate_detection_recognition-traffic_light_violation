const Navbar = () => {
    return <div>
        <div style={{ width: '100%', height: '100%', paddingLeft: 28, paddingRight: 28, paddingTop: 20, paddingBottom: 20, justifyContent: 'space-between', alignItems: 'center', display: 'inline-flex' }}>
            <div style={{ justifyContent: 'flex-start', alignItems: 'flex-start', display: 'flex' }}>
                <div style={{ color: 'rgba(255, 255, 255, 0.40)', fontSize: 16, fontFamily: 'Inter', fontWeight: '400', lineHeight: 18, wordWrap: 'break-word' }}>© 2023 Trinetra</div>
            </div>
            <div style={{ borderRadius: 8, justifyContent: 'flex-start', alignItems: 'center', gap: 16, display: 'flex' }}>
                <div style={{ color: 'rgba(255, 255, 255, 0.40)', fontSize: 16, fontFamily: 'Inter', fontWeight: '400', lineHeight: 18, wordWrap: 'break-word' }}>About</div>
                <div style={{ color: 'rgba(255, 255, 255, 0.40)', fontSize: 16, fontFamily: 'Inter', fontWeight: '400', lineHeight: 18, wordWrap: 'break-word' }}>Support</div>
                <div style={{ color: 'rgba(255, 255, 255, 0.40)', fontSize: 16, fontFamily: 'Inter', fontWeight: '400', lineHeight: 18, wordWrap: 'break-word' }}>Contact Us</div>
            </div>
        </div>
    </div>
}
export default Navbar;