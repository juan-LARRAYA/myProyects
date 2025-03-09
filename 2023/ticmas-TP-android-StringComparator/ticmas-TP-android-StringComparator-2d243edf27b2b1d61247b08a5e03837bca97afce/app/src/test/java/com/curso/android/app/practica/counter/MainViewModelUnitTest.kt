package com.curso.android.app.practica.counter

import androidx.arch.core.executor.testing.InstantTaskExecutorRule
import com.curso.android.app.practica.counter.view.MainViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.test.*
import org.junit.After
import org.junit.Assert.*
import org.junit.Before
import org.junit.Rule
import org.junit.Test

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * See [testing documentation](http://d.android.com/tools/testing).
 */
@OptIn(kotlinx.coroutines.ExperimentalCoroutinesApi::class)
class MainViewModelUnitTest {

    private lateinit var viewModel: MainViewModel

    @get:Rule
    val instantTaskRule = InstantTaskExecutorRule()
    private val dispatcher = StandardTestDispatcher()

    @Before
    fun setup() {
        Dispatchers.setMain(dispatcher)
        viewModel = MainViewModel()
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    @Test
    fun mainViewModel_CheckInitialValue() = runTest {
        val sonIguales = viewModel.stringComparator.value?.sonIguales
        assertEquals(false, sonIguales)
    }

    @Test
    fun useViewModelMethod() {
        val sonIguales = viewModel.areEqual()
        viewModel.updateComparison("hola", "hello")
        assertEquals(false, sonIguales)
        viewModel.updateComparison("hola", "hola")
        assertEquals(false, sonIguales)
    }
}