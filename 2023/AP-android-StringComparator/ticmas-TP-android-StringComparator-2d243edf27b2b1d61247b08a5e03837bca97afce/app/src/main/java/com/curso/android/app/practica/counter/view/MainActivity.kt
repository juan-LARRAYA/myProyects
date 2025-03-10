package com.curso.android.app.practica.counter.view

import android.os.Bundle
import android.view.View
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import com.curso.android.app.practica.counter.R
import com.curso.android.app.practica.counter.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding
    private val mainViewModel: MainViewModel by viewModels()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        mainViewModel.stringComparator.observe(this) {
            binding.messageTextView.visibility = View.VISIBLE
            if (mainViewModel.areEqual()) {
                binding.messageTextView.text = getString(R.string.AreEqual)
            } else {
                binding.messageTextView.text = getString(R.string.AreDifferent)
            }
        }
        binding.compButton.setOnClickListener {
            mainViewModel.updateComparison(
                binding.Text.text.toString(),
                binding.Text2.text.toString()
            )
        }
    }
}

