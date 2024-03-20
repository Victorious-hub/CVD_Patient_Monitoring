package com.example.cvd_monitoring.presentation.current_user

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.domain.use_case.current_user.CurrentUserUseCase
import com.example.cvd_monitoring.presentation.CurrentUserState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class CurrentUserViewModel @Inject constructor(
    private val currentUserUseCase: CurrentUserUseCase,
) : ViewModel() {
    private val _state = mutableStateOf(CurrentUserState())
    val state: State<CurrentUserState> = _state

    fun getCurrentUser(slug: String) {
        viewModelScope.launch {
            try {
                val currentUser = currentUserUseCase(slug)
                _state.value = CurrentUserState(currentUser)
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("PatientListViewModel", errorMessage, e)
            }
        }
    }
}