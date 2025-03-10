package com.curso.android.app.practica.counter.view

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.curso.android.app.practica.counter.model.StringComparator
import kotlinx.coroutines.launch

class MainViewModel : ViewModel() {
    val stringComparator: LiveData<StringComparator> get() = _stringComparator
    private val _stringComparator =
        MutableLiveData<StringComparator>(StringComparator(null, null, false))

    fun updateComparison(text1: String, text2: String) {
        viewModelScope.launch {
            _stringComparator.value = StringComparator(text1, text2, (text1 == text2))
        }
    }

    fun areEqual(): Boolean {
        return _stringComparator.value!!.sonIguales
    }
}
