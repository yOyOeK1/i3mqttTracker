# i3mqttTracker

**project in early stage / working**

My way to get connection with my iot and i3 / i3status bar. Python orientated plugin / service. Running in back ground and on define action on mqtt layer update your i3status box.

### now in basic setup

![](./examples/screen1.png)

Section `| i3mqtt: ...... 70% |` all can by customized.

## using it

* set up i3mqttTracker.py - mqtt_config, TARGET_FILE (use some tmpfs to not kill hard drive) by editing file
  **default TARGET_FILE** - /run/user/1000/i3mqtt.line

* start i3mqttTracker.py - it will push new data to `TARGET_FILE`

* add to your `~/.config/i3status/config` lines
  
  ```bash
  ...
  order += "read_file i3mqtt"
  read_file i3mqtt {
      format = "i3mqtt: %content"
      path = "/run/user/1000/i3mqtt.line"
  }
  ...
  ```

## development of package - base line

  In directory of project to deploy ...

  ```shell
  i3mqttTracker
  ├── examples
  │   └── screen1.png
  ├── i3mqttCmd.sh
  ├── i3mqttTracker.py
  ├── LICENSE
  ├── README.md
  └── requirements.txt
  ```


### TODO
  - [ ] unify config place
  - [x] make some info about how to run / setup
  - [x] update to repository 

---

If you see that this makes sense [ send me a ☕ ](https://ko-fi.com/B0B0DFYGS) | [Master repository](https://github.com/yOyOeK1/oiyshTerminal) | [About SvOiysh](https://www.youtube.com/@svoiysh)
