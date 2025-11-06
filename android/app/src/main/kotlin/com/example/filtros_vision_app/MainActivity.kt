package com.example.filtros_vision_app

import android.os.Handler
import android.os.Looper
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel
import java.io.File
import java.io.FileOutputStream
import java.util.concurrent.Executors

class MainActivity : FlutterActivity() {
    private val CHANNEL = "com.example.filtros_vision_app/opencv"
    private val executor = Executors.newFixedThreadPool(4)
    private val mainHandler = Handler(Looper.getMainLooper())
    private lateinit var filterProcessor: ImageFilterProcessor

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)
        
        filterProcessor = ImageFilterProcessor()

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, CHANNEL).setMethodCallHandler { call, result ->
            when (call.method) {
                "applyFilter" -> {
                    val imagePath = call.argument<String>("imagePath")
                    val filterName = call.argument<String>("filterName")
                    val parameters = call.argument<Map<String, Any>>("parameters") ?: emptyMap()

                    if (imagePath == null || filterName == null) {
                        mainHandler.post { result.error("INVALID_ARGUMENT", "Missing required arguments", null) }
                        return@setMethodCallHandler
                    }

                    executor.execute {
                        try {
                            val processedBytes = filterProcessor.processImage(imagePath, filterName, parameters)
                            
                            if (processedBytes != null) {
                                val outputFile = File(cacheDir, "processed_${System.currentTimeMillis()}.jpg")
                                FileOutputStream(outputFile).use { it.write(processedBytes) }
                                
                                mainHandler.post { result.success(outputFile.absolutePath) }
                            } else {
                                mainHandler.post { result.error("PROCESSING_ERROR", "Failed to process image", null) }
                            }
                        } catch (e: Exception) {
                            e.printStackTrace()
                            mainHandler.post { result.error("EXCEPTION", e.message, null) }
                        }
                    }
                }
                else -> {
                    mainHandler.post { result.notImplemented() }
                }
            }
        }
    }

    override fun onDestroy() {
        super.onDestroy()
        executor.shutdown()
    }
}
