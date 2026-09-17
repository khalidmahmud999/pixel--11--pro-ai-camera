name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.10'
      - uses: actions/setup-java@v4
        with:
          distribution: 'zulu'
          java-version: '17'
      - name: Install deps
        run: |
          pip install buildozer cython==0.29.33
          sudo apt update
          sudo apt install -y zip unzip
      - name: Accept Licenses
        run: |
          p=$ANDROID_HOME/cmdline-tools/latest/bin
          export PATH=$p:$PATH
          yes | sdkmanager --licenses || true
          sdkmanager "build-tools;37.0.0"
          sdkmanager "platforms;android-33"
      - name: Build APK
        run: |
          mkdir -p ~/.android/licenses
          mkdir -p ~/.buildozer/android/platform/android-sdk/licenses
          echo "8933bad161af4178b1185d1a37fbf41ea5269c55" > ~/.android/licenses/android-sdk-license
          echo "d56f5187479451eabf01fb78af6dfcb131a6481e" >> ~/.android/licenses/android-sdk-license
          echo "24333f8a63b6825ea9c5514f83c1059b8ea4b097" >> ~/.android/licenses/android-sdk-license
          cp ~/.android/licenses/* ~/.buildozer/android/platform/android-sdk/licenses/ || true
          cp $ANDROID_HOME/licenses/* ~/.android/licenses/ || true
          cp $ANDROID_HOME/licenses/* ~/.buildozer/android/platform/android-sdk/licenses/ || true
          buildozer -v android debug
      - name: Upload APK
        uses: actions/upload-artifact@v4
        with:
          name: Pixel11-Pro-APK
          path: bin/*.apk
