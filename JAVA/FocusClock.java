import java.awt.*;
import java.swing.*;

public class FocusClock extends JFrame{
  private JLabel timeLabel;
  private int minutes, seconds;
  
  public FocusClock(int minutes) {
    this.minutes = minutes;
    this.seconds = 0;
    timeLabel = new JLabel(getTimeString());
    timeLabel.setHorizontalAlignment(JLabel.CENTER);
    setDefaulCloseOperation(JFrame.EXIT_ON_CLOSE);
    setSize(300, 200);
    setVisible(true);
    startCountdown();
  }
  
  private String getTimeString() {
    return String.format("%02d:%02d", minutes, seconds);
  }
  
  private void startCountdown() {
    Timer timer = new Timer(1000, e -> {
      if (seconds == 0) {
        if (minutes == 0) {
          // 倒计时完成
          JOptionPane.showMessageDialog(this, "Time is up!");
          System.exit(0);
        } else {
          minutes--;
          seconds = 59;
        }
      } else {
        seconds--;
      }
      timeLabel.setText(getTimeString());
    });
    timer.start();
  }
  
  public static void main(String[] args) {
    int minutes = Integer.parseInt(JOptionPane.showInputDialog("Enter the number of minutes to focus:"));
    new FocusClock(minutes);
  }
}
    
