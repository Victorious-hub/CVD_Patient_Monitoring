package com.example.cvd_monitoring.presentation.doctor_contact

import android.util.Log
import androidx.compose.runtime.State
import androidx.compose.runtime.mutableStateOf
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.cvd_monitoring.common.TextFieldState
import com.example.cvd_monitoring.domain.use_case.current_user.CurrentUserUseCase
import com.example.cvd_monitoring.domain.use_case.doctor_update.DoctorContactUseCase
import com.example.cvd_monitoring.presentation.CurrentUserState
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class DoctorContactViewModel @Inject constructor(
    private val doctorContactUseCase: DoctorContactUseCase,
    private val currentUserUseCase: CurrentUserUseCase
) : ViewModel() {
    private val _firstNameState = mutableStateOf(TextFieldState())
    val firstNameState: State<TextFieldState> = _firstNameState

    fun setFirstNameValue(value: String) {
        _firstNameState.value = firstNameState.value.copy(text = value)
    }

    private val _lastNameState = mutableStateOf(TextFieldState())
    val lastNameState: State<TextFieldState> = _lastNameState

    fun setLastNameValue(value: String) {
        _lastNameState.value = lastNameState.value.copy(text = value)
    }

    private val _emailState = mutableStateOf(TextFieldState())
    val emailState: State<TextFieldState> = _emailState

    fun setEmailValue(value: String) {
        _emailState.value = emailState.value.copy(text = value)
    }

    private val _mobileState = mutableStateOf(TextFieldState())
    val mobileState: State<TextFieldState> = _mobileState

    fun setMobileValue(value: String) {
        _mobileState.value = mobileState.value.copy(text = value)
    }

    private val _state = mutableStateOf(CurrentUserState())
    val state: State<CurrentUserState> = _state

    fun getCurrentUser(slug: String) {
        viewModelScope.launch {
            try {
                val currentUser = currentUserUseCase(slug)
                _state.value = CurrentUserState(currentUser)
                state.value.patient?.user?.let { setEmailValue(it.email) }
                state.value.patient?.user?.let { setFirstNameValue(it.first_name) }
                state.value.patient?.user?.let { setLastNameValue(it.last_name) }
                state.value.patient?.let { setMobileValue(it.mobile) }
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("PatientListViewModel", errorMessage, e)
            }
        }
    }

    fun updateDoctorContact(slug: String) {
        val firstName = firstNameState.value.text
        val lastName = lastNameState.value.text
        val email = emailState.value.text

        viewModelScope.launch {
            try {
                val createdUser = doctorContactUseCase(firstName, lastName, email, slug)
                Log.d("SignUpViewModel", "Sign up successful: $createdUser")
            } catch (e: Exception) {
                val errorMessage = e.message.toString()
                Log.e("SignUpViewModel", "Sign up error: $errorMessage", e)
            }
        }
    }
}