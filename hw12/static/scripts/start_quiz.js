function startQuiz() {
    if (sessionStorage.getItem('startTime')) {
        sessionStorage.removeItem('startTime');  // Clear the timer
        $('#timerDisplay').hide();  // Hide the timer display when not active
    }
}
$(document).ready(function () {
    const startTime = sessionStorage.getItem('startTime');
    if (startTime) {
        const endTime = Date.now();
        const elapsed = endTime - parseInt(startTime);
        const seconds = Math.floor((elapsed / 1000) % 60);
        const minutes = Math.floor((elapsed / 1000 / 60) % 60);
        $('#timerDisplay').text(`Total Learning Time: ${minutes} minutes, ${seconds} seconds`);
        $('#timerDisplay').css('display', 'block');  // Show the timer display when active
        $('#timerDisplay').addClass('alert alert-success');  // Add a green background to the timer display
    } else {
        $('#timerDisplay').text(''); // Clears the timer display when not active
        $('#timerDisplay').hide();  // Hide the timer display when not active
    }
});