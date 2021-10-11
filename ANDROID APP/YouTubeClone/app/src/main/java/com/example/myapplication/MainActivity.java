package com.example.myapplication;

import android.app.Activity;
import android.os.Bundle;
import android.webkit.WebViewClient;
import android.webkit.WebChromeClient;
import android.webkit.WebView;
import android.webkit.WebSettings;


import com.example.myapplication.R;

public class MainActivity extends Activity {
  private WebView mwebView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        

//webview

mwebView=(WebView) findViewById(R.id.webv);

WebSettings webSettings = mwebView.getSettings();

mwebView.loadUrl("https://www.youtube.com/");
webSettings.setJavaScriptEnabled(true);
mwebView.setWebViewClient(new WebViewClient()
);
    }

}
